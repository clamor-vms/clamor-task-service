package models

import (
	"github.com/jinzhu/gorm"
)

// Task Group Task
type Task struct {
	gorm.Model

	ID          uint   `gorm:"primary_key"`
	Name        string `gorm:"size:255"`
	Description string
	UserID      int    
	TaskGroupID int    
}
