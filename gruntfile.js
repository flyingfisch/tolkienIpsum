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
    });

    grunt.loadNpmTasks('grunt-contrib-sass');

    grunt.registerTask('default', ['sass']);
}
