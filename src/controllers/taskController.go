package controllers

import (
	"net/http"
	"os"

	skaioskit "github.com/nathanmentley/skaioskit-go-core"

	"skaioskit/core"
)

// TaskController structure of TaskController
type TaskController struct {
}

// NewTaskController testing
func NewTaskController() *TaskController {
	return &TaskController{}
}

// Get basic information
func (p *TaskController) Get(w http.ResponseWriter, r *http.Request) skaioskit.ControllerResponse {
	return skaioskit.ControllerResponse{Status: http.StatusOK, Body: GetAboutResponse{
		Name:        "Skaioskit Task Service",
		CoreVersion: skaioskit.VERSION,
		Version:     core.SERVICE_VERSION,
		BuildTime:   os.Getenv("BUILD_DATETIME"),
	}}
}
