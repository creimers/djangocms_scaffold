/**
* Created by arinker on 01.06.15.
*/
module.exports = function (gulp, wiredep) {
  return function (cb) {
    gulp.src('pyjade_project/templates/base.jade')
    .pipe(wiredep({
      ignorePath: '../static/',
      directory: 'pyjade_project/static/bower_components',
      fileTypes: {
        jade: {
          detect: {
            js: /script\(.*src=['"]([^'"]+)/gi,
            css: /link\(.*href=['"]([^'"]+)/gi
          },
          replace: {
            js: 'script(src=\'{{ STATIC_URL }}{{filePath}}\')',
            css: 'link(rel=\'stylesheet\', href=\'{{ STATIC_URL }}{{filePath}}\')'
          }
        },
      },
    }))
    .pipe(gulp.dest('pyjade_project/templates'))
    .on('finish', cb);
  };
};
