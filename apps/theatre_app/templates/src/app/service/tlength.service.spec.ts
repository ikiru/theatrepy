import { TestBed, inject } from '@angular/core/testing';

import { TlengthService } from './tlength.service';

describe('TlengthService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TlengthService]
    });
  });

  it('should be created', inject([TlengthService], (service: TlengthService) => {
    expect(service).toBeTruthy();
  }));
});
