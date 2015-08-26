/**
* Created by arinker on 01.06.15.
*/
module.exports = function (gulp, plugins, config) {
  return function (cb) {
    gulp.src([config.static_root + 'main.scss'])
    .pipe(plugins.sass({
      errLogToConsole: true
    }))
    .pipe(gulp.dest(config.static_root));
    cb();
  };
};
