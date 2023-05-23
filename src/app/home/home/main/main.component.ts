import { Component } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent {
  offset = 1;
  limit = 2;
  imageUrl = "./assets/R.jpeg"
}
