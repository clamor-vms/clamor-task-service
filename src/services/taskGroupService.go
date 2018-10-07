package services

import (
    "github.com/jinzhu/gorm"

    "skaioskit/models"
)

type ITaskGroupService interface {
    CreateTaskGroup(models.TaskGroup) models.TaskGroup
    UpdateTaskGroup(models.TaskGroup) models.TaskGroup
    GetTaskGroup(uint) (models.TaskGroup, error)
    GetTaskGroups() ([]models.TaskGroup, error)
    EnsureTaskGroupTable()
}

// TaskGroupService 
type TaskGroupService struct {
    db *gorm.DB
}

// NewTaskGroupService 
func NewTaskGroupService(db *gorm.DB) *TaskGroupService {
    return &TaskGroupService{db: db}
}

// CreateTaskGroup 
func (p *TaskGroupService) CreateTaskGroup(taskGroup models.TaskGroup) models.TaskGroup {
    p.db.Create(&taskGroup)
    return taskGroup
}

// UpdateTaskGroup 
func (p *TaskGroupService) UpdateTaskGroup(taskGroup models.TaskGroup) models.TaskGroup {
    p.db.Save(&taskGroup)
    return taskGroup
}

// GetTaskGroup 
func (p *TaskGroupService) GetTaskGroup(name string) (models.TaskGroup, error) {
    var taskGroup models.TaskGroup
    err := p.db.Where(&models.TaskGroup{Name: name}).First(&taskGroup).Error
    return taskGroup, err
}

func (p *TaskGroupService) GetTaskGroups() ([]models.TaskGroup, error) {
    var taskGroups []models.TaskGroup
    err := p.db.Preload("TaskGroup").Find(&taskGroups).Error
    return taskGroups, err
}

// EnsureTaskGroupTable	...
func (p *TaskGroupService) EnsureTaskGroupTable() {
    p.db.AutoMigrate(&models.TaskGroup{})
}

// EnsureTaskGroup	test
func (p *TaskGroupService) EnsureTaskGroup(taskGroup models.TaskGroup) {
    existing, err := p.GetTaskGroup(taskGroup.Name)
    if err != nil {
        p.CreateTaskGroup(taskGroup)
    } else {
        existing.Name = taskGroup.Name
        p.UpdateTaskGroup(existing)
    }
}