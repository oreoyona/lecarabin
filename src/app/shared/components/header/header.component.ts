import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { MatDialog, MatDialogConfig, MatDialogRef } from '@angular/material/dialog';
import { MenuComponent } from './menu/menu.component';
import { SearchComponent } from './search/search.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit, OnChanges {

  logo = "/assets/lecarabin-logo.svg";
  widthValue = ""; screenHeight!: number; screenWidth!: number;

  config: MatDialogConfig = {
    height: "100vh",
    width: this.widthValue,
    position: { top: "0", left: '0' }

  }
  openMenu = () => {
    this.dialog.open(MenuComponent, { height: "100vh", width: this.widthValue, position: { top: '0', left: '0' } })
  }

  openSearch = () => {
    this.dialog.open(SearchComponent, {
      height: "100vh", width: this.widthValue,
      position: { top: '0', right: '0' },

    })
  }


  constructor(public dialog: MatDialog) { }
  ngOnInit() {
    this.screenHeight = window.innerHeight
    this.screenWidth = window.innerWidth
    window.addEventListener('resize', this.onResize.bind(this));
    this.screenWidth > 800 ? this.widthValue = "40vw" : this.widthValue = "100vw";

  }


  ngOnChanges(): void {
    this.screenHeight = window.innerHeight
    this.screenWidth = window.innerWidth
    this.screenWidth > 800 ? this.widthValue = "40vw" : this.widthValue = "100vw"

  }

  onResize() {
    this.ngOnChanges();
  }


}
