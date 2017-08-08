import { TestBed, inject } from '@angular/core/testing';

import { AuditionService } from './audition.service';

describe('AuditionService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AuditionService]
    });
  });

  it('should be created', inject([AuditionService], (service: AuditionService) => {
    expect(service).toBeTruthy();
  }));
});
