import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SinglePostComponent} from './single-post/single-post.component';
import { SinglePageComponent } from './single-page/single-page.component';
import { EditArticleComponent } from './edit-article/edit-article.component';
import { PagesRoutingModule } from './pages-routing.module';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { ShowArticleComponent } from './show-article/show-article.component';

@NgModule({
  declarations: [
    SinglePostComponent,
    SinglePageComponent,
    EditArticleComponent,
    ShowArticleComponent,
  ],
  imports: [
    CommonModule,
    PagesRoutingModule,
    MatFormFieldModule,
    MatIconModule,

  ]
})
export class PagesModule { }
