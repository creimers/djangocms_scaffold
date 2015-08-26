'use strict';
/**
 * Created by arinker on 01.06.15.
 */
var gulp = require('gulp');
var plugins = require('gulp-load-plugins')();
var wiredep = require('wiredep').stream;

var usemin = require('gulp-jade-usemin');
var uglify = require('gulp-uglify');
var minifyCss = require('gulp-minify-css');
var rev = require('gulp-rev');

var task_folder = './_gulp_tasks/';

var config = {
    path: {
        sources: 'sources/',
        compiled: 'compiled/',
        dist: 'distribution/'
        },
    ignore: '!./sources/bower_components/**/*',
    static_root: 'pyjade_project/static/',
};

gulp.task('wiredep',  require(task_folder + 'django_wiredep')(gulp, wiredep));
gulp.task('compileSCSS', require(task_folder + 'compileSCSS')(gulp, plugins, config));
gulp.task('usemin', require(task_folder + 'usemin')(gulp, usemin, minifyCss, uglify, rev));

gulp.task('watch', [
  'compileSCSS',
  'wiredep'
  ], function () {
    gulp.watch(['**/*.scss', config.ignore], ['compileSCSS']);
    gulp.watch('bower.json', ['wiredep']);
});

gulp.task('build', ['compileSCSS', 'wiredep', 'usemin'], function () {
});

gulp.task('develop', ['compileSCSS', 'wiredep'], function () {
});

gulp.task('default', ['develop'], function () {
    console.log(config.ignore)
});

