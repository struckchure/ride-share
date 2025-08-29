package handler

import (
	"context"

	"github.com/labstack/echo/v4"
	"github.com/struckchure/location-service/models"
	"gorm.io/gorm"
)

type Rider struct {
	db *gorm.DB
}

func (r *Rider) List(c echo.Context) error {
	ctx := context.Background()
	riders, err := gorm.G[models.Rider](r.db).Find(ctx)
	if err != nil {
		return c.JSON(500, err)
	}

	return c.JSON(200, riders)
}

func (r *Rider) Create(c echo.Context) error {
	var rider models.Rider

	err := c.Bind(&rider)
	if err != nil {
		return c.JSON(400, err)
	}

	ctx := context.Background()
	err = gorm.G[models.Rider](r.db).Create(ctx, &rider)

	if err != nil {
		return c.JSON(500, err)
	}

	return c.JSON(201, rider)
}

func (r *Rider) Update(c echo.Context) error {
	var rider models.Rider

	err := c.Bind(&rider)
	if err != nil {
		return c.JSON(400, err)
	}

	ctx := context.Background()
	_, err = gorm.G[models.Rider](r.db).Where("id = ?", rider.ID).Select("Name", "Age").Updates(ctx, rider)

	if err != nil {
		return c.JSON(500, err)
	}

	return c.JSON(202, rider)
}

func NewRider(db *gorm.DB) *Rider {
	return &Rider{db: db}
}
