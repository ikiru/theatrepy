import { TestBed, inject } from '@angular/core/testing';

import { ThonorService } from './thonor.service';

describe('ThonorService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ThonorService]
    });
  });

  it('should be created', inject([ThonorService], (service: ThonorService) => {
    expect(service).toBeTruthy();
  }));
});
