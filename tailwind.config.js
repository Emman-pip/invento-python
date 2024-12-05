/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./invento/**/*.{html,js}",
    "./invento/**./**/*.{html,js}",
    "./invento/**/**./**/*.{html,js}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
