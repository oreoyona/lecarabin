import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SinglePostComponent } from './single-post/single-post.component';
import { SinglePageComponent } from './single-page/single-page.component';
import { EditArticleComponent } from './edit-article/edit-article.component';
import { PagesRoutingModule } from './pages-routing.module';
import { MatFormFieldModule } from '@angular/material/form-field';

@NgModule({
  declarations: [
    SinglePostComponent,
    SinglePageComponent,
    EditArticleComponent
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    MatFormFieldModule,

  ]
})
export class PagesModule { }
