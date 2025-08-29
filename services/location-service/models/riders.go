package models

type Rider struct {
	ID   uint    `gorm:"primaryKey" json:"id" param:"id"`
	Name string  `json:"name"`
	Lat  float32 `json:"lat"`
	Lng  float32 `json:"lng"`
}
