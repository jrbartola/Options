import { createMuiTheme } from '@material-ui/core';

const desktopFontSize = 18;

export const desktopTheme = createMuiTheme({
  overrides: {
    // Name of the component
    MuiInputBase: {
      formControl: { fontSize: desktopFontSize }
    },
    MuiFormLabel: { root: { fontSize: 16, marginTop: 2 } },
    MuiFormControlLabel: {
      root: { fontSize: 16 },
      label: { fontSize: desktopFontSize }
    },
    MuiSvgIcon: { fontSizeSmall: { fontSize: 20 } },
    MuiSelect: {
      outlined: { paddingRight: '24px !important' },
      iconOutlined: { right: 4, fontSize: 24 }
    },
    MuiMenuItem: {
      root: { fontSize: desktopFontSize }
    }
  }
});

const mobileFontSize = 12;

export const mobileTheme = createMuiTheme({
  overrides: {
    // Name of the component
    MuiInputBase: {
      formControl: { fontSize: mobileFontSize }
    },
    MuiFormLabel: { root: { fontSize: mobileFontSize, marginTop: 0 } },
    MuiFormControlLabel: {
      root: { fontSize: mobileFontSize },
      label: { fontSize: mobileFontSize }
    },
    MuiSvgIcon: { fontSizeSmall: { fontSize: 20 } },
    MuiSelect: {
      outlined: { paddingRight: '24px !important' },
      iconOutlined: { right: 4, fontSize: 24 }
    },
    MuiMenuItem: {
      root: { fontSize: mobileFontSize }
    }
  }
});
