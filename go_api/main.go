package main

import (
	"database/sql"
	"encoding/json"
	"log"
	"net/http"

	_ "modernc.org/sqlite"
)

type Signal struct {
	Symbol        string  `json:"symbol"`
	Date          string  `json:"date"`
	Signal        string  `json:"signal"`
	Direction     string  `json:"direction"`
	Pattern       string  `json:"pattern"`
	Close         float64 `json:"close"`
	NextDayReturn float64 `json:"next_day_return"`
}
type DirectionPerformance struct {
	Direction   string  `json:"direction"`
	TotalTrades int     `json:"total_trades"`
	AvgReturn   float64 `json:"avg_return"`
	WinRate     float64 `json:"win_rate"`
}


func getSignalsHandler(w http.ResponseWriter, r *http.Request) {
	symbol := r.URL.Query().Get("symbol")
	direction := r.URL.Query().Get("direction")

	db, err := sql.Open("sqlite", "data/trading.db")
	if err != nil {
	log.Println("database query error:", err)
	http.Error(w, "database query error", http.StatusInternalServerError)
	return
}
	defer db.Close()

	query := `
	SELECT symbol, date, signal, direction, pattern, close, next_day_return
	FROM signals
`

	conditions := []string{}
	args := []interface{}{}

	if symbol != "" {
		conditions = append(conditions, "symbol = ?")
		args = append(args, symbol)
	}

	if direction != "" {
		conditions = append(conditions, "direction = ?")
		args = append(args, direction)
	}

	if len(conditions) > 0 {
		query += " WHERE " + conditions[0]

		for i := 1; i < len(conditions); i++ {
			query += " AND " + conditions[i]
		}
	}
		

	rows, err := db.Query(query, args...)
	if err != nil {
		http.Error(w, "database query error", http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	signals := []Signal{}

	for rows.Next() {
		var s Signal

		err := rows.Scan(
			&s.Symbol,
			&s.Date,
			&s.Signal,
			&s.Direction,
			&s.Pattern,
			&s.Close,
			&s.NextDayReturn,
		)

		if err != nil {
			http.Error(w, "row scan error", http.StatusInternalServerError)
			return
		}

		signals = append(signals, s)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(signals)
}
func getPerformanceHandler(w http.ResponseWriter, r *http.Request) {
	symbol := r.URL.Query().Get("symbol")

	db, err := sql.Open("sqlite", "data/trading.db")
	if err != nil {
		log.Println("database connection error:", err)
		http.Error(w, "database connection error", http.StatusInternalServerError)
		return
	}
	defer db.Close()

	query := `
		SELECT
			direction,
			COUNT(*) AS total_trades,
			AVG(next_day_return) AS avg_return,
			AVG(CASE WHEN next_day_return > 0 THEN 1.0 ELSE 0.0 END) AS win_rate
		FROM signals
		WHERE symbol = ?
		GROUP BY direction
	`

	rows, err := db.Query(query, symbol)
	if err != nil {
		log.Println("database query error:", err)
		http.Error(w, "database query error", http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	results := []DirectionPerformance{}

	for rows.Next() {
		var p DirectionPerformance

		err := rows.Scan(
			&p.Direction,
			&p.TotalTrades,
			&p.AvgReturn,
			&p.WinRate,
		)

		if err != nil {
			log.Println("row scan error:", err)
			http.Error(w, "row scan error", http.StatusInternalServerError)
			return
		}

		results = append(results, p)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(results)
}
func main() {
	http.HandleFunc("/signals", getSignalsHandler)
	http.HandleFunc("/performance", getPerformanceHandler)

	log.Println("Go API running on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
