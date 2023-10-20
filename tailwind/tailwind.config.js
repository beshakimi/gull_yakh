/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../addProducts/templates/**/*.html"],
  theme: {
    extend: {},

    fontFamily: {
      vazir: ["vazir", "sans-serif"],
      vazirBold: ["vazirBold", "sans-serif"],
      vazirMed: ["vazirMed", "sans-serif"],
      vazirLight: ["vazirLight", "sans-serif"],
    },
  },
  plugins: [],
};
