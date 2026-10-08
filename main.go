package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// 接口：GET /api/user
	r.GET("/api/user", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"code": 200,
			"msg":  "success",
			"data": gin.H{
				"name": "test",
				"id":   1001,
			},
		})
	})

	// 监听8888端口
	r.Run(":8888")
}