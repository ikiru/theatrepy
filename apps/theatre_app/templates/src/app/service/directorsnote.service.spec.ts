import { TestBed, inject } from '@angular/core/testing';

import { DirectorsnoteService } from './directorsnote.service';

describe('DirectorsnoteService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DirectorsnoteService]
    });
  });

  it('should be created', inject([DirectorsnoteService], (service: DirectorsnoteService) => {
    expect(service).toBeTruthy();
  }));
});
