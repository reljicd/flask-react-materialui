import { red } from '@mui/material/colors';
import { createTheme } from '@mui/material/styles';

// A custom theme for this react-app
const theme = createTheme({
  palette: {
    primary: {
      main: '#556cd6',
    },
    secondary: {
      main: '#19857b',
    },
    error: {
      main: red.A400,
    },
  },
});

export default theme;
