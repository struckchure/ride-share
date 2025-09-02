package main

import (
	"log"

	_ "github.com/joho/godotenv/autoload"

	"github.com/labstack/echo/v4"
	"github.com/struckchure/location-service/handler"
	"github.com/struckchure/location-service/lib"
	"github.com/struckchure/location-service/models"
)

func main() {
	db := lib.NewDatabase()
	err := db.AutoMigrate(&models.Rider{})
	if err != nil {
		log.Panic(err)
	}

	riderHandler := handler.NewRider(db)

	e := echo.New()

	e.GET("/riders", riderHandler.List)
	e.POST("/riders", riderHandler.Create)
	e.PATCH("/riders", riderHandler.Update)

	e.Logger.Fatal(e.Start(":8081"))
}
