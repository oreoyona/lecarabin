import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-imageless-article',
  templateUrl: './imageless-article.component.html',
  styleUrls: ['./imageless-article.component.scss']
})
export class ImagelessArticleComponent {
  @Input () title!:string;
}
