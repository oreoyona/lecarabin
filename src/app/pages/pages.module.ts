import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SinglePostComponent } from './single-post/single-post.component';
import { SinglePageComponent } from './single-page/single-page.component';



@NgModule({
  declarations: [
    SinglePostComponent,
    SinglePageComponent
  ],
  imports: [
    CommonModule
  ]
})
export class PagesModule { }
