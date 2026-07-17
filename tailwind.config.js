/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{html,js}"],
  theme: {
    extend: {
      textShadow: {
        '3d': `
          1px 1px 0px #e2cca6,
          2px 2px 0px #e2cca6,
          3px 3px 0px #e2cca6,
          4px 4px 0px #e2cca6,
          5px 5px 0px #e2cca6,
          6px 6px 0px #e2cca6,
          7px 7px 0px #310c0c, /* Borde final oscuro para dar profundidad */
          8px 8px 0px #310c0c
        `,
      },
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

