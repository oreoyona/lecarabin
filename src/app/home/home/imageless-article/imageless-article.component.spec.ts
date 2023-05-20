import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImagelessArticleComponent } from './imageless-article.component';

describe('ImagelessArticleComponent', () => {
  let component: ImagelessArticleComponent;
  let fixture: ComponentFixture<ImagelessArticleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ImagelessArticleComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ImagelessArticleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
