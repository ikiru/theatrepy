import { TestBed, inject } from '@angular/core/testing';

import { VocaltypeService } from './vocaltype.service';

describe('VocaltypeService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [VocaltypeService]
    });
  });

  it('should be created', inject([VocaltypeService], (service: VocaltypeService) => {
    expect(service).toBeTruthy();
  }));
});
