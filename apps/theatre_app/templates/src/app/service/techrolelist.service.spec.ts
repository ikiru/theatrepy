import { TestBed, inject } from '@angular/core/testing';

import { TechrolelistService } from './techrolelist.service';

describe('TechrolelistService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TechrolelistService]
    });
  });

  it('should be created', inject([TechrolelistService], (service: TechrolelistService) => {
    expect(service).toBeTruthy();
  }));
});
