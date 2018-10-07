/*
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU Affero General Public License as
   published by the Free Software Foundation, either version 3 of the
   License, or (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Affero General Public License for more details.

   You should have received a copy of the GNU Affero General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

package controllers

import (
	"net/http"
	"encoding/json"
	"strconv"
	"os"

	skaioskit "github.com/nathanmentley/skaioskit-go-core"
	"skaioskit/core"
	"skaioskit/services"
)

// TaskGroupController
type TaskGroupController struct {
	taskGroupService services.ITaskGroupService
}

// NewTaskGRoupController create controller and handle model / service
func NewTaskGroupController(taskGroupService services.ITaskGroupService) *TaskGroupController {
	return &TaskGroupController{
		taskGroupService: taskGroupService,
	}
}

// Get
func (p *TaskGroupController) Get(w http.ResponseWriter, r *http.Request) skaioskit.ControllerResponse {

	idStr, ok := r.URL.Query()["id"]

	if ok {
		id, err := strconv.ParseUint(idStr[0], 10, 32)
		if err == nil {
			taskGroup, err := p.taskGroupService.GetTaskGroup(uint(id))
			if err == nil {
				return skaioskit.ControllerResponse{Status: http.StatusOK, Body: taskGroup}
			}
		}
	} else {
		taskGroups, err := p.taskGroupService.GetTaskGroups()
		if err == nil {
			return skaioskit.ControllerResponse{Status: http.StatusOK, Body: GetTaskGroupResponse{TaskGroups: taskGroups}}
		}
	}
	
	return skaioskit.ControllerResponse{Status: http.StatusNotFound, Body: skaioskit.EmptyResponse{}}


	// return skaioskit.ControllerResponse{Status: http.StatusOK, Body: GetAboutResponse{
	// 	Name:        "Clamour task group controller basic return",
	// 	CoreVersion: skaioskit.VERSION,
	// 	Version:     core.SERVICE_VERSION,
	// 	BuildTime:   os.Getenv("BUILD_DATETIME"),
	// }}
}

// Post
func (p *TaskGroupController) Post(w http.ResponseWriter, r *http.Request) skaioskit.ControllerResponse {
	return skaioskit.ControllerResponse{Status: http.StatusNotFound, Body: skaioskit.EmptyResponse{}}
}

// Put
func (p *TaskGroupController) Put(w http.ResponseWriter, r *http.Request) skaioskit.ControllerResponse {
	return skaioskit.ControllerResponse{Status: http.StatusNotFound, Body: skaioskit.EmptyResponse{}}
}

// Delete
func (p *TaskGroupController) Delete(w http.ResponseWriter, r *http.Request) skaioskit.ControllerResponse {
	return skaioskit.ControllerResponse{Status: http.StatusNotFound, Body: skaioskit.EmptyResponse{}}
}
