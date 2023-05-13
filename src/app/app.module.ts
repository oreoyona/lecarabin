import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeaderComponent } from './shared/components/header/header.component';
import { FooterComponent } from './shared/components/footer/footer.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule} from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatDialogModule} from '@angular/material/dialog';
import { MatListModule } from '@angular/material/list';
import { MatInputModule} from '@angular/material/input'
import { MenuComponent } from './shared/components/header/menu/menu.component';
import { SearchComponent } from './shared/components/header/search/search.component';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    MenuComponent,
    SearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatIconModule,
    MatDialogModule,
    MatListModule,
    MatInputModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
