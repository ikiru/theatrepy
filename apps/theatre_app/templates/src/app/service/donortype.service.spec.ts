import { TestBed, inject } from '@angular/core/testing';

import { DonortypeService } from './donortype.service';

describe('DonortypeService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [DonortypeService]
    });
  });

  it('should be created', inject([DonortypeService], (service: DonortypeService) => {
    expect(service).toBeTruthy();
  }));
});
