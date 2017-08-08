import { TestBed, inject } from '@angular/core/testing';

import { GradyearService } from './gradyear.service';

describe('GradyearService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GradyearService]
    });
  });

  it('should be created', inject([GradyearService], (service: GradyearService) => {
    expect(service).toBeTruthy();
  }));
});
