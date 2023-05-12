import { Component } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { MenuComponent } from './menu/menu.component';
import { SearchComponent } from './search/search.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {

  logo = "/assets/lecarabin-logo.svg";
  config: MatDialogConfig = {
    height: "100vh",
    width: "40vw",
    position: {top: "0", left: '0'}

  }
  openMenu = () =>{
    this.dialog.open(MenuComponent, this.config)
  }

  openSearch = () => {
    this.dialog.open(SearchComponent, {height: "100vh", width: "40vw",position: {top: '0', right: '0'}})
  }


  constructor(public dialog: MatDialog){}
}
