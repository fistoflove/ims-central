const sass = require('node-sass');

module.exports = function (grunt) {
    grunt.initConfig({
      sass: {
        options: {
            implementation: sass,
            sourceMap: true
        },
        core: {
          files: {
            "app/static/css/base.css": "scss/base.scss"
          },
        },
      },
      watch: {
        files: [
          "scss/*"
        ],
        tasks: [
          "sass",
        ],
      },
    });
    grunt.loadNpmTasks("grunt-sass");
    grunt.loadNpmTasks("grunt-contrib-watch");
  };
  
  