import * as React from 'react';
import { IconButton, Menu, MenuItem } from '@material-ui/core';
import SettingsIcon from '@material-ui/icons/Settings';
import TokenDialog from './TokenDialog';

const SettingsMenu = () => {
  const [tokenModalOpen, setTokenModalOpen] = React.useState<boolean>(false);
  const [menuAnchor, setMenuAnchor] = React.useState<null | HTMLElement>(null);
  const open = Boolean(menuAnchor);

  const openMenu = (event: React.MouseEvent<HTMLElement>) => {
    setMenuAnchor(event.currentTarget);
  };

  const closeMenu = () => {
    setMenuAnchor(null);
  };

  const closeTokenModal = () => {
    setTokenModalOpen(false);
  };

  return (
    <>
      <TokenDialog
        isOpen={tokenModalOpen}
        onClose={closeTokenModal}
        onSave={closeTokenModal}
      />
      <IconButton onClick={openMenu} color="inherit">
        <SettingsIcon />
      </IconButton>
      <Menu
        id="nav-settings"
        anchorEl={menuAnchor}
        anchorOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        keepMounted
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
        open={open}
        onClose={() => setMenuAnchor(null)}
      >
        <MenuItem onClick={() => setTokenModalOpen(true)}>Set token</MenuItem>
      </Menu>
    </>
  );
};

export default SettingsMenu;
