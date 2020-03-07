# React/Material UI demo app created using Python

Source code is transpiled from Python to JavaScript using [Transcrypt](https://www.transcrypt.org).  The standard JavaScript libraries below are are used directly from the Python code.  Lightweight wrapper modules were created to keep the Python code as clean and pythonic as possible.   To keep the toolchain simple, and again to keep code in the Python world, JSX was _not_ used.

```pip install transcrypt```

JavaScript dependencies can be installed with npm using package.json in the repository

* react
* react-dom
* react-number-format
* @material-ui/core
* lodash
* notistack
* parcel-bundler
* parcel-plugin-transcrypt

The toolchain uses Parcel for transpiling the Python code and bundling the result along with the standard Javascript libraries.  The [parcel-bundler plugin for Transcrypt](https://www.npmjs.com/package/parcel-plugin-transcrypt) made this process pretty smooth.

dev build:

```npx parcel --log-level 4 --no-cache src/index.html --out-dir build```

production build:

```npx parcel build build/index.html --no-source-maps --out-dir build/public --public-url ./```

