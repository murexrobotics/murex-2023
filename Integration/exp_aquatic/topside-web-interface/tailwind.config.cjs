/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      backgroundImage: {
        'murex-gif': "url('/src/MUREX.gif')"
      },
      colors: {
        'dark-blue': '#25283D',
        'light-blue': '#59C3C3',
        'red': '#A54657',
        'yellow': '#F6BD60',
        'white': '#EBEBEB',
      }
    }
  },
  plugins: []
};