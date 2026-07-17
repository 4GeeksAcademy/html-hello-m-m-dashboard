/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "canyon-sand": "#eceff1",
        "soft-cream": "#eceff1",
        "coyote-shadow": "#263238",
        "acme-red": "#c62828",
        "runner-orange": "#00acc1",
        "bankruptcy-red": "#c62828",
        "bruise-purple": "#00acc1",
        "anvil-gray": "#455a64"
      }
    },
  },
  plugins: [],
}

