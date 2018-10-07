package models

import (
	"github.com/jinzhu/gorm"
)

// TaskGroup Model
type TaskGroup struct {
	gorm.Model

	CampaignID  int
	ID          uint   `gorm:"primary_key"`
	Name        string `gorm:"size:255"`
	Description string
	Tasks 		[]Task `gorm:"foreignkey:TaskGroupID;association_foreignkey:TaskGroupID"`
}
