module.exports = function(gulp, usemin, minifyCss, uglify, rev) {
  return function(cb){
    gulp.src('pyjade_project/templates/base.jade')
    .pipe(usemin({
      css: [minifyCss(), 'concat'],
      js: [uglify(), rev()],
    }))
    .pipe(gulp.dest('build/'))
    .on('finish', cb);
  } 
};
