import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowArticleComponent } from './show-article.component';

describe('ShowArticleComponent', () => {
  let component: ShowArticleComponent;
  let fixture: ComponentFixture<ShowArticleComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ShowArticleComponent]
    });
    fixture = TestBed.createComponent(ShowArticleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
