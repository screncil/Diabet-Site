module.exports = {
  content: ['./src/**/*.{vue,js,ts,jsx,tsx}', './index.html', "./node_modules/flowbite/**/*.js"],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
}