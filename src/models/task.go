package models

import (
	"github.com/jinzhu/gorm"
)

// Task Group Task
type Task struct {
	gorm.Model

	UserID      int    `gorm:"index"`
	TaskGroupID int    `gorm:"index"`
	ID          uint   `gorm:"primary_key"`
	Name        string `gorm:"size:255"`
	Description string `gorm:"size:2500"`
}
