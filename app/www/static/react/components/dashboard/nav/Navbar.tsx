import * as React from 'react';
import { Toolbar, AppBar, Typography, makeStyles } from '@material-ui/core';
import SettingsMenu from './SettingsMenu';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(2),
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

const Navbar = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Option Finder
          </Typography>
          <SettingsMenu />
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default Navbar;
