import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-header-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent {
  categories = ['Opinions', 'Actualites', 'Cas Cliniques', 'Livres']

}
