import { TestBed, inject } from '@angular/core/testing';

import { TpositionService } from './tposition.service';

describe('TpositionService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TpositionService]
    });
  });

  it('should be created', inject([TpositionService], (service: TpositionService) => {
    expect(service).toBeTruthy();
  }));
});
