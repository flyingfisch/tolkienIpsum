module.exports = function(grunt) {

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        sass: {
            dist: {
                options: {
                    trace: true
                },
                files: {
                    'static/tolkienIpsum/css/site.css': 'static/tolkienIpsum/sass/site.scss'
                }
            }
        },
        cssmin: {
            options: {
                roundingPrecision: -1
            },
            target: {
                files: {
                    'static/tolkienIpsum/css/site.min.css': 'static/tolkienIpsum/css/site.css'
                }
            }
        },
        watch: {
            scripts: {
                files: ['**/*'],
                tasks: ['default']
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['sass', 'cssmin']);
}
