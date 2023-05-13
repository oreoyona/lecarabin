import { Component } from '@angular/core';

@Component({
  selector: 'app-header-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent {
  categories = ['Opinions', 'Actualites', 'Cas Cliniques', 'Livres']

}
