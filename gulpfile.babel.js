
var gulp          = require('gulp');
var uglify        = require('gulp-uglify');
var yargs         = require('yargs');
var browserSync   = require('browser-sync').create();
var $             = require('gulp-load-plugins')();
var autoprefixer  = require('autoprefixer');
var webpack       = require("webpack");
var webpackStream = require('webpack-stream');


// Check for --production flag
const PRODUCTION = !!(yargs.argv.production);

var sassPaths = [
  'node_modules/foundation-sites/scss',
  'node_modules/motion-ui/src'
];

var destination = 'pykapela/app/static/';

let webpackConfig = {
  mode: (PRODUCTION ? 'production' : 'development'),
  module: {
    rules: [
      {
        test: /\.js$/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [ "@babel/preset-env" ],
            compact: false
          }
        }
      }
    ]
  },
  devtool: !PRODUCTION && 'source-map'
}

function sass() {
  return gulp.src('pykapela/src/assets/scss/app.scss')
    .pipe($.sass({
      includePaths: sassPaths,
      outputStyle: 'compressed' // if css compressed **file size**
    })
      .on('error', $.sass.logError))
    // .pipe($.postcss([
    //   autoprefixer({ browsers: ['last 2 versions', 'ie >= 9'] })
    // ]))
    .pipe(gulp.dest(destination + 'assets/css'))
    .pipe(browserSync.stream());
};

// Combine JavaScript into one file
// In production, the file is minified
function javascript() {
  return gulp.src('pykapela/src/assets/js/app.js')
    //.pipe(named())
    .pipe($.sourcemaps.init())
    .pipe(webpackStream(webpackConfig, webpack))
    .pipe($.if(PRODUCTION, $.terser()
       .on('error', e => { console.log(e); })
    ))
    .pipe($.if(!PRODUCTION, $.sourcemaps.write()))
    .pipe(gulp.dest(destination + 'assets/js'));
}

function asset_files() {
  return gulp.src('pykapela/src/assets/img/*.*')
      .pipe(gulp.dest(destination + 'assets/img'))
}

function serve() {
  browserSync.init({
    proxy: "localhost:8000",
    port: 8000,
    notify: false,
  });

  gulp.watch("pykapela/src/assets/scss/*.scss", sass);
  gulp.watch("pykapela/src/assets/scss/*/*.scss", sass);
  gulp.watch("pykapela/src/assets/js/*.js").on('change', browserSync.reload);
  gulp.watch("pykapela/templates/*.html").on('change', browserSync.reload);
  gulp.watch("pykapela/templates/*/*.html").on('change', browserSync.reload);
  gulp.watch("pykapela/templates/*/*/*.html").on('change', browserSync.reload);

}

gulp.task('runserver', function() {
  var proc = exec('python manage.py runserver')
});

gulp.task('sass', sass);
gulp.task('start', gulp.series('sass', asset_files, javascript, serve));
gulp.task('default', gulp.series('sass', asset_files, javascript, serve));
gulp.task('build', gulp.series('sass', asset_files, javascript));