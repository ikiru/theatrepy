import { TestBed, inject } from '@angular/core/testing';

import { TrankService } from './trank.service';

describe('TrankService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TrankService]
    });
  });

  it('should be created', inject([TrankService], (service: TrankService) => {
    expect(service).toBeTruthy();
  }));
});
