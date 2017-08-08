import { TestBed, inject } from '@angular/core/testing';

import { SpecialskillsService } from './specialskills.service';

describe('SpecialskillsService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SpecialskillsService]
    });
  });

  it('should be created', inject([SpecialskillsService], (service: SpecialskillsService) => {
    expect(service).toBeTruthy();
  }));
});
